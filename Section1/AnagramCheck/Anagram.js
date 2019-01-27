var word1 = [];
var word2 = [];

$("#check").click(function() {
  var word1 = $("#word1")
    .val()
    .replace(/\s+/g, "")
    .replace(/[.,\/#!?'$%\^&\*;:{}=\-_`~()]/g, "")
    .toLowerCase()
    .split("")
    .sort()
    .join();
  var word2 = $("#word2")
    .val()
    .replace(/\s+/g, "")
    .replace(/[.,\/#!?'$%\^&\*;:{}=\-_`~()]/g, "")
    .toLowerCase()
    .split("")
    .sort()
    .join();
  if (word1 === word2) {
    $("#answer")
      .empty()
      .append("<p>This is an anagram.</p>");
  } else {
    $("#answer")
      .empty()
      .append("<p>This is not an anagram.</p>");
  }
});
