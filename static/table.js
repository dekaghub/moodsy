$(function() {
    console.log("ready");

    var list = $( "#input_data" ).text();
    console.log(list);

    document.getElementById("song1").innerHTML = list[0];
    document.getElementById("song2").innerHTML = list[1];
    document.getElementById("song3").innerHTML = list[2];
    
    // var dragHandler = function(evt){
    //     evt.preventDefault();
    // };

    // var dropHandler = function(evt){
    //     evt.preventDefault();
    //     var files = evt.originalEvent.dataTransfer.files;

    //     var formData = new FormData();
    //     formData.append("file2upload", files[0]);

    //     var req = {
    //         url: "/sendfile",
    //         method: "post",
    //         processData: false,
    //         contentType: false,
    //         data: formData
    //     };

    //     var promise = $.ajax(req);
    // };

    // var dropHandlerSet = {
    //     dragover: dragHandler,
    //     drop: dropHandler
    // };

    // $(".droparea").on(dropHandlerSet);
});