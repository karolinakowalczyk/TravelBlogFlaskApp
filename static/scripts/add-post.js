let addPostForm = document.getElementsByClassName("content-area");

document.addEventListener("keypress", function (e) {
  if (e.target.tagName === "TEXTAREA") {
    return true;
  }
  if (e.keyCode === 13 || e.which === 13) {
    e.preventDefault();
    return false;
  }
});

let hashtagInput = document.querySelector("#hashtag-input");
let hashtagsContainer = document.querySelector(".hashtags-container");
let deleteTagBtn = document.querySelectorAll(".hashtag-btn");
let deleteTags = document.querySelectorAll(".hashtag-el");

function addHashTag(URL, requestOptions) {
  fetch(URL, requestOptions)
    .then((response) => console.log(response.json()))
    .catch((err) => console.log(err));
}

function removeHashTag(URL, requestOptions) {
  fetch(URL, requestOptions)
    .then((response) => console.log(response.json()))
    .catch((err) => console.log(err));
}

if (hashtagInput) {
  hashtagInput.addEventListener("keypress", function (event) {
    if (event.keyCode === 13 && hashtagInput.value.length > 0) {
      let hashValue = hashtagInput.value;
      let hashText = document.createTextNode("#" + hashValue);
      let hashButtonText = document.createTextNode("X");
      let hashDiv = document.createElement("div");
      let hashParagraph = document.createElement("p");
      let hashButton = document.createElement("div");
      hashButton.appendChild(hashButtonText);
      hashtagsContainer.appendChild(hashDiv);
      hashDiv.appendChild(hashParagraph);
      hashDiv.appendChild(hashButton);
      hashParagraph.appendChild(hashText);
      hashDiv.classList.add("hashtag-el");
      hashButton.classList.add("hashtag-btn");
      hashParagraph.classList.add("hashtag-p");

      let requestOptions = {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          hashtag: hashValue,
        }),
      };

      hashButton.addEventListener("click", () => {
        hashtagsContainer.removeChild(hashDiv);
        removeHashTag("/remove-hashtag", requestOptions);
      });
      hashtagInput.value = "";

      addHashTag("/add-hashtag", requestOptions);
    }
  });
}
