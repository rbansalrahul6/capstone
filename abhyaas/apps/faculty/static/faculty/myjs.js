// var main_page = ["Dashboard", "Settings", "Logout"];

// var course_page = ["Course Notes", "Assignment", "Inbox", "Logout"];

(function() {
  'use strict';
  var dialogButton = document.querySelector('.mdl-button');
  var dialog = document.querySelector('#new-message');
  if (! dialog.showModal) {
    dialogPolyfill.registerDialog(dialog);
  }
  dialogButton.addEventListener('click', function() {
     //alert("asd");
     dialog.showModal();
  });
  dialog.querySelector('button:not([disabled])')
  .addEventListener('click', function() {
    dialog.close();
  });
}());