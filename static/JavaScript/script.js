const mySlider = document.getElementById("my-slider");
const sliderValue = document.getElementById("slider-value");

function slider(){
    let valPercent = (mySlider.value / mySlider.max)*100;
    console.log(valPercent)
    mySlider.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue.textContent = mySlider.value;

}
slider();

const mySlider2 = document.getElementById("my-slider2");
const sliderValue2 = document.getElementById("slider-value2");

function slider2(){
    let valPercent = (mySlider2.value / mySlider2.max)*100;
    console.log("deuxoeddkd")
    console.log(valPercent)
    mySlider2.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue2.textContent = mySlider2.value;

}
slider2();


const mySlider3 = document.getElementById("my-slider3");
const sliderValue3 = document.getElementById("slider-value3");

function slider3(){
    let valPercent = (mySlider3.value / mySlider3.max);
    console.log("deuxoeddkd")
    console.log(valPercent)
    mySlider3.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue3.textContent = mySlider3.value;

}
slider3();

const mySlider4 = document.getElementById("my-slider4");
const sliderValue4 = document.getElementById("slider-value4");

function slider4(){
    let valPercent = (mySlider4.value / mySlider4.max);
    console.log("deuxoeddkd")
    console.log(valPercent)
    mySlider4.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
    sliderValue4.textContent = mySlider4.value;

}
slider4();


document.getElementById("gene").onclick = function(event){

    X = [1,2,3,4,5,6,7,8,9,10]
    Y = [2,4,6,8,10,12,14, 16,18,20]
    document.getElementById("inputs").innerHTML = ""
    document.getElementById("inputs").innerHTML = ""
    for (let i =0; i < 10; i++){
        document.getElementById("inputs").value += X[i];
        document.getElementById("outputs").value += Y[i];
        if (i < 9){
            document.getElementById("inputs").value += ","
            document.getElementById("outputs").value += ","


        } 
            
        }


        event.preventDefault();
    
};




document.getElementById("myForm").addEventListener("submit", function(event) {
    function estimerTemp(iteration){
      if (iteration >= 5000){
        let time_nominal = 2.7
        let value_nominal = 5000
        let resultat = (iteration / value_nominal) * time_nominal
        return resultat;
      } 

      else{
        return 2
      }

    }

    let estimation = estimerTemp(mySlider3.value);
    decret = true
    function decrementer(){
      if (estimation > 0){
        estimation --;
        console.log("est", estimation)
        document.getElementById("estimation").innerHTML = `il reste environ ${estimation.toFixed(2)} sec`;
      }

    }
    event.preventDefault(); // Empêche l'envoi du formulaire

    let label = document.getElementById("verdict")
    document.getElementById("verdict").innerHTML = "Patientez pendant que nous formons votre model...";
    label.style.color = "blue";
    console.log("estimation : ", estimation)

    setInterval(decrementer, 1000)
    
    document.getElementById("estimation").innerHTML = estimation;


    let inputs = document.getElementById("inputs").value; // Récupérer le texte du textarea
    let outputs = document.getElementById("outputs").value; // Récupérer le texte du textarea

    //let lg = document.getElementById("lg").value;

    fetch("/", { method: "POST", body: new FormData(document.getElementById("myForm")) })
      .then(response => response.json())
      .then(data => {
        console.log(data.result);
        let resultModel = data.result;
        console.log("finish")
        let label = document.getElementById("verdict")
        if (resultModel["verdict"] == 0){
          document.getElementById("verdict").innerHTML = "Error";
          label.style.color = "red";
          estimation = 0
          document.getElementById("estimation").innerHTML = "0 sec"

        }
        else if(resultModel["verdict"] == 1){
          document.getElementById("verdict").innerHTML = "Entrainnement Reussi ! <br> Vous pouvez maintenant effectuer une test sous la Rubrique prediction.";
          label.style.color = "green";
          estimation = 0
          document.getElementById("estimation").innerHTML = "0 sec"

        }
        else{
          document.getElementById("verdict").innerHTML = "Error";
          label.style.color = "red";
          document.getElementById("estimation").innerHTML = "0 sec"

          estimation = 0
        }
        



        //document.getElementById("resultTextArea").value = textePrecedent + " " + resultModel;
      });
   // document.getElementById("resultTextArea").value = ""; // Réinitialiser le textarea
  });

document.getElementById("myForm1").addEventListener("submit", function(event) {

  event.preventDefault(); // Empêche l'envoi du formulaire

  fetch("/executer_code", { method: "POST", body: new FormData(document.getElementById("myForm1")) })
  .then(response => response.json())
  .then(data => {
    console.log(data.result);
    let resultModel = data.result;
    document.getElementById("value_predict").value = resultModel['prediction'][0][0].toFixed(2)



    //document.getElementById("resultTextArea").value = textePrecedent + " " + resultModel;
  });



});

