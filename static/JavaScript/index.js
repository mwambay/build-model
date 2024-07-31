console.log("hello")
document.getElementById("myForm").addEventListener("submit", function(event) {

    event.preventDefault(); // Empêche l'envoi du formulaire
    let input = document.getElementById("inp").value;
    console.log("hello");

    fetch("/", { method: "POST", body: new FormData(document.getElementById("myForm")) })
      .then(response => response.json())
      .then(data => {
        let resultModel = data.result;

        //console.log(data.result);
        //let resultModel = data.result;
        for (let i = 0; i<10; i++){
          console.log(i)
        }

        document.getElementById("value_predict").value += resultModel['hello'];
        
   // document.getElementById("resultTextArea").value = ""; // Réinitialiser le textarea
  });

});