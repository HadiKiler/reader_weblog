document.addEventListener("DOMContentLoaded", function () {
    let chunk_size = 4 * 1000 * 1000;
    let next_chunk = chunk_size;
    let current_slice = 0;
    let current_chunk = 0;
    let file_size = 0;
    let left_size = 0;
    let repeat = 0;
    let url = 'http://127.0.0.1:8000/admin/blog/post/edit/2/';
    let final = 0;

    let file = document.getElementById("file");
    document.getElementsByTagName("form")[0].addEventListener("submit", function (event) {
        event.preventDefault();
        file_size = file.files[0].size;
        left_size = file.files[0].size;
        repeat = Math.floor(file.files[0].size / chunk_size) + 1;
        
        for (let i = 0; i < repeat; i++) {
            let form_data = new FormData();
            form_data.append('csrfmiddlewaretoken', document.querySelector('input[name="csrfmiddlewaretoken"]').value);
            if (i === repeat - 1)
                final = 1;
            form_data.append('final', final);
            form_data.append('ali', 'ali');

            if (current_chunk + chunk_size > file_size) {
                current_slice = file.files[0].slice(current_chunk, file_size);
                form_data.append('current_slice', current_slice);
                $.ajax({
                    url: url,
                    data: form_data,
                    method: "POST",
                    dataType: "json",
                    cache: false,
                    processData: false,
                    contentType: false,
                    success: function (context) {

                    },
                    error: function () {

                    }
                });
            } else {
                current_slice = file.files[0].slice(current_chunk, next_chunk);
                form_data.append('current_slice', current_slice);
                $.ajax({
                    url: url,
                    data: form_data,
                    method: "POST",
                    dataType: "json",
                    cache: false,
                    processData: false,
                    contentType: false,
                    success: function (context) {

                    },
                    error: function () {

                    }
                });
            }
            console.log(current_slice);
            current_chunk = next_chunk;
            next_chunk = current_chunk + chunk_size;
            left_size -= chunk_size;
        }
    });
});
