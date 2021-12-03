console.log("this is connected");

const result = document.querySelector(".result");
const form = document.getElementById("form");
const message = document.getElementById("message");

const avg_rss12 = document.getElementById("avg_rss12");
const var_rss12 = document.getElementById("var_rss12");
const avg_rss13 = document.getElementById("avg_rss13");
const var_rss13 = document.getElementById("var_rss13");
const avg_rss23 = document.getElementById("avg_rss23");
const var_rss23 = document.getElementById("var_rss23");

const arr = [avg_rss12, var_rss12, avg_rss13, var_rss13, avg_rss23, var_rss23];

form.addEventListener("submit", (e) => {
  output = checkInputs();
  console.log(output);
  if (output === "error") {
    e.preventDefault();
  }
});

function checkInputs() {
  // get all the values
  const avg_rss12Value = avg_rss12.value.trim();
  const var_rss12Value = var_rss12.value.trim();
  const avg_rss13Value = avg_rss13.value.trim();
  const var_rss13Value = var_rss13.value.trim();
  const avg_rss23Value = avg_rss23.value.trim();
  const var_rss23Value = var_rss23.value.trim();

  let message;
  if (avg_rss12Value === "") {
    // show error
    // add error class
    msg = "This feild cannot be blank";
    setError(avg_rss12, msg);
    message = "error";
  } else {
    // add succuss class
    setSuccess(avg_rss12);
  }

  if (var_rss12Value === "") {
    // show error
    // add error class
    msg = "This feild cannot be blank";
    setError(var_rss12, msg);
    message = "error";
  } else {
    // add succuss class
    setSuccess(var_rss12);
  }

  if (avg_rss13Value === "") {
    // show error
    // add error class
    msg = "This feild cannot be blank";
    setError(avg_rss13, msg);
    message = "error";
  } else {
    // add succuss class
    setSuccess(avg_rss13);
  }
  if (var_rss13Value === "") {
    // show error
    // add error class
    msg = "This feild cannot be blank";
    setError(var_rss13, msg);
    message = "error";
  } else {
    // add succuss class
    setSuccess(var_rss13);
  }
  if (avg_rss23Value === "") {
    // show error
    // add error class
    msg = "This feild cannot be blank";
    setError(avg_rss23, msg);
    message = "error";
  } else {
    // add succuss class
    setSuccess(avg_rss23);
  }
  if (var_rss23Value === "") {
    // show error
    // add error class
    msg = "This feild cannot be blank";
    setError(var_rss23, msg);
    message = "error";
  } else {
    // add succuss class
    setSuccess(var_rss23);
  }
  if (message === "error") {
    return message;
  }
}

function setError(input, message) {
  const formField = input.parentElement; // .form-feild
  const small = formField.querySelector("small");

  // add error message in small tag
  small.innerText = message;

  // add error class
  formField.classList.remove("Success");
  formField.classList.add("Error");
}

function setSuccess(input) {
  const formField = input.parentElement; // .form-feild
  formField.classList.remove("Error");
  formField.classList.add("Success");
}
