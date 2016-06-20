$(document).ready(function () {
  $( "#comments" ).resizable({
    handles: "se",
    containment: "#container",
    maxWidth: 300,
    maxHeight: 100
  });

  $( "#description" ).resizable({
    handles: "se",
    containment: "#container",
    maxWidth: 300,
    maxHeight: 100
  });
});

var submitting = false;

function checkForm(form)
{
  if(form.user.value == "") {
    alert("Please enter your first and last names");
    form.user.focus();
    return false;
  }
  
  return true;
}

function resetForm(form)
{
  form.myButton.disabled = false;
  form.myButton.value = "Submit";
  submitting = false;
}