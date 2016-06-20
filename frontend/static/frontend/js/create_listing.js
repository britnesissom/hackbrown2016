var submitting = false;

function checkForm(form)
{
  if(form.user.value == "") {
    alert("Please enter the name of this listing.");
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