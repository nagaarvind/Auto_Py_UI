const mainFileBtn = document.getElementById("main-file");
const uploadBtn = document.getElementById("upload-Btn");
const uploadTxt = document.getElementById("upload-text");

uploadBtn.addEventListener("click", function () {
  mainFileBtn.click();
});
mainFileBtn.addEventListener("change", function () {
  if (mainFileBtn.value) {
    uploadTxt.innerHTML = mainFileBtn.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1]; //regex
  } else {
    uploadTxt.innerHTML = "No File choosen";
  }
});
