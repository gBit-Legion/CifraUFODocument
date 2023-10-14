<style scoped>
form {
    display: block;
    height: 400px;
    width: 400px;
    background: #ccc;
    margin: auto;
    margin-top: 40px;
    text-align: center;
    line-height: 400px;
    border-radius: 4px;
}

div.file-listing {
    width: 400px;
    margin: auto;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

div.file-listing img {
    height: 100px;
    display: block;
}

div.remove-container {
    text-align: center;
}

div.remove-container a {
    color: red;
    cursor: pointer;
}

a.submit-button {
    display: block;
    margin: auto;
    text-align: center;
    width: 200px;
    padding: 10px;
    text-transform: uppercase;
    background-color: #CCC;
    color: white;
    font-weight: bold;
    margin-top: 20px;
}

progress {
    width: 400px;
    margin: auto;
    display: block;
    margin-top: 20px;
    margin-bottom: 20px;
}
</style>

<template>
    <div id="file-drag-drop">
        <h2>Drag And Drop</h2>
        <hr />
        <form id="drop-form" @drop="handleFileDrop($event)">
            <span class="drop-files">Drop the files here!</span>
        </form>

        <div v-for="(file, key) in files" v-bind:key="'file-' + key" class="file-listing">
            <img class="preview" v-bind:id="'drag-and-drop-preview-' + parseInt(key)" />
            {{ file.name }}
            <div class="remove-container">
                <a class="remove" v-on:click="removeFile(key)">Remove</a>
            </div>
        </div>

        <progress max="100" :value.prop="uploadPercentage"></progress>

        <a class="submit-button" v-on:click="submitFiles()" v-show="files.length > 0">Submit</a>
    </div>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="photo">
        <input type="submit" value="Submit">
    </form>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            dragAndDropCapable: false,
            files: [],
            uploadPercentage: 0
        }
    },

    mounted() {
        /*
            Определите, поддерживается ли в браузере функция перетаскивания.
        */
        this.dragAndDropCapable = this.determineDragAndDropCapable();

        /*
            Если возможно перетаскивание, мы продолжаем привязывать события к нашим элементам.
        */
        if (this.dragAndDropCapable) {
            this.bindEvents();
        }
    },

    methods: {
        bindEvents() {
            /*
                Прослушивайте все события перетаскивания и привязывайте прослушиватель событий к каждому.
для файловой формы.
            */
            ['drag', 'dragstart', 'dragend', 'dragover', 'dragenter', 'dragleave', 'drop'].forEach(function (evt) {
                /*
                    Для каждого события добавьте прослушиватель событий, который предотвращает действие по умолчанию.
(открыв файл в браузере) и остановить распространение события (так
никакие другие элементы не открывают файл в браузере)
                */
                document.getElementById('drop-form').addEventListener(evt, function (e) {
                    e.preventDefault();
                    e.stopPropagation();
                }.bind(this), false);
            }.bind(this));
        },

        handleFileDrop(event) {
            for (let i = 0; i < event.dataTransfer.files.length; i++) {
                this.files.push(event.dataTransfer.files[i]);
            }

            this.getImagePreviews();
        },

        determineDragAndDropCapable() {
            /*
                Создайте тестовый элемент, чтобы проверить, являются ли определенные события
присутствуют, что позволяет нам перетаскивать.
            */
            var div = document.createElement('div');

            /*
                Проверьте, находится ли событие `перетаскивания` в элементе.
или события ondragstart и ondrop находятся в элементе. Если
они есть, значит у нас есть то, что нам нужно для перетаскивания файлов.

Мы также проверяем, есть ли в окне объекты FormData и FileReader.
присутствует, чтобы мы могли выполнить загрузку AJAX
            */
            return (('draggable' in div)
                || ('ondragstart' in div && 'ondrop' in div))
                && 'FormData' in window
                && 'FileReader' in window;
        },

        getImagePreviews() {
            /*
                Переберите все файлы и создайте предварительный просмотр изображения для каждого из них.
            */
            for (let i = 0; i < this.files.length; i++) {
                /*
                    Убедитесь, что файл является файлом изображения.
                */
                if (/\.(jpe?g|png|gif)$/i.test(this.files[i].name)) {
                    /*
                        Создайте новый объект FileReader.
                    */
                    let reader = new FileReader();

                    /*
                        Добавьте прослушиватель событий, когда файл был загружен.
                         чтобы обновить src при предварительном просмотре файла.
                    */
                    reader.addEventListener("load", function () {
                        document.getElementById('drag-and-drop-preview-' + parseInt(i)).src = reader.result;
                    }.bind(this), false);

                    /*
                        Считайте данные файла через устройство чтения. Когда оно имеет
                         загружено, мы слушаем распространяемое событие и устанавливаем изображение
                         src к тому, что было загружено из ридера.
                    */
                    reader.readAsDataURL(this.files[i]);
                } else {
                    /*
                        Мы делаем следующий тик, чтобы ссылка была привязана и мы могли получить к ней доступ.
                    */
                    this.$nextTick(function () {
                        document.getElementById('drag-and-drop-preview-' + parseInt(i)).src = '/images/file.png';
                    });
                }
            }
        },

        removeFile(key) {
            this.files.splice(key, 1);
            this.getImagePreviews();
        },

        submitFiles() {
            /*
                Инициализируйте данные формы
            */
            let formData = new FormData();

            /*
                Перебрать любой файл, отправленный после добавления файлов.
                 к данным формы.
            */
            for (var i = 0; i < this.files.length; i++) {
                let file = this.files[i];

                formData.append('files[' + i + ']', file);
            }

            /*
                Сделайте запрос к URL-адресу POST /file-drag-drop.
            */
            axios.post('http://26.234.143.237:8080/documents',
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    },
                    onUploadProgress: function (progressEvent) {
                        this.uploadPercentage = parseInt(Math.round((progressEvent.loaded / progressEvent.total) * 100));
                    }.bind(this)
                }
            ).then(function () {
                console.log('SUCCESS!!');
            })
                .catch(function () {
                    console.log('FAILURE!!');
                });
        }
    }
}

    
</script>