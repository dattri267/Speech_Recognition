const recordBtn = document.getElementById("record-btn");
const stopBtn = document.getElementById("stop-btn");
const predictBtn = document.getElementById("predict-btn");

const statusText = document.getElementById("status-text");

const audioPlayer = document.getElementById("audio-player");

const resultCard = document.getElementById("result-card");

const emotionResult = document.getElementById("emotion-result");

const confidenceFill = document.getElementById("confidence-fill");

const confidenceText = document.getElementById("confidence-text");


let mediaRecorder;
let audioChunks = [];
let recordedBlob = null;

recordBtn.addEventListener("click", async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true,
    });

    mediaRecorder = new MediaRecorder(stream);

    audioChunks = [];

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
      recordedBlob = new Blob(audioChunks,{
      type: mediaRecorder.mimeType
      });
    
    console.log(recordedBlob.type);
    console.log(recordedBlob.size);

    console.log(mediaRecorder.mimeType);

      const audioURL = URL.createObjectURL(recordedBlob);

      audioPlayer.src = audioURL;

      audioPlayer.style.display = "block";

      statusText.textContent = "Recording completed.";
    };

    mediaRecorder.start();

    statusText.textContent = "Recording...";
  } catch (error) {
    alert("Microphone permission denied.");
  }
});
stopBtn.addEventListener("click",()=>{

    if(mediaRecorder &&
       mediaRecorder.state==="recording"){

        mediaRecorder.stop();

    }

});
predictBtn.addEventListener("click", async () => {

    if (!recordedBlob) {

        alert("Please record audio first.");

        return;
    }

    statusText.textContent = "Analyzing emotion...";

    const formData = new FormData();

    formData.append(
        "audio",
        recordedBlob,
        "recording.webm"
    );

    try {

        const response = await fetch("/predict", {

            method: "POST",

            body: formData

        });

        const data = await response.json();
        console.log(data);

        if (data.error) {

            alert(data.error);

            statusText.textContent = "Prediction failed.";

            return;

        }

        resultCard.classList.add("show");

        emotionResult.textContent = data.emotion;

        confidenceFill.style.width = data.confidence + "%";

        confidenceText.textContent = data.confidence + "%";

        statusText.textContent = "Prediction completed.";

    }

    catch (error) {

        console.error(error);

        alert("Unable to connect to the server.");

    }

});
