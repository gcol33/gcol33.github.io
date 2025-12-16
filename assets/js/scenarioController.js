const locationOptions = ["random", "protected"];
const mortalityLabels = ["low", "medium", "high"];
const mortalityFunctions = ["constant", "exponential"]; // Updated from "linear" to "constant"

// Update slider value labels
function updateValue(slider, labelId) {
  document.getElementById(labelId).textContent = slider.value;
}

function updateMortalityLabel(slider) {
  const label = mortalityLabels[slider.value];
  document.getElementById("mortality_label_val").textContent = label;
}

function toggleCapacityVisibility() {
  const mortality_func =
    mortalityFunctions[document.getElementById("mortality_func").value];
  const capacityContainer = document.getElementById("capacityContainer");

  if (mortality_func === "constant") {
    capacityContainer.style.display = "none";
  } else {
    capacityContainer.style.display = "block";
  }
}

function updateMedia() {
  const pairs = document.getElementById("pairs").value;
  const location = locationOptions[document.getElementById("location").value];
  const mortality_label =
    mortalityLabels[document.getElementById("mortality_label").value];
  const mortality_func =
    mortalityFunctions[document.getElementById("mortality_func").value];

  let combo_id;

  if (mortality_func === "constant") {
    combo_id = `Pairs${pairs}_${location}_${mortality_label}_${mortality_func}`;
  } else {
    const capacity = document.getElementById("capacity").value;
    combo_id = `Pairs${pairs}_${location}_K${capacity}_${mortality_label}_${mortality_func}`;
  }

  const imagePath = "assets/scenario_plots/" + combo_id + ".jpg";
  const videoPath = "assets/scenario_videos/" + combo_id + ".mp4";

  console.log("✅ Image path:", imagePath);
  console.log("✅ Video path:", videoPath);

  const image = document.getElementById("scenarioImage");
  const video = document.getElementById("scenarioVideo");
  const source = document.getElementById("videoSource");

  // Preload image
  const preloadImage = new Image();
  preloadImage.src = imagePath;
  preloadImage.onload = () => {
    image.src = imagePath;
  };

  // Preload video if source has changed
  const currentVideoSrc = source.getAttribute("src");
  if (videoPath !== currentVideoSrc) {
    const preloadVideo = document.createElement("video");
    preloadVideo.muted = true;
    preloadVideo.autoplay = true;
    preloadVideo.loop = true;
    preloadVideo.playsInline = true;

    const preloadSource = document.createElement("source");
    preloadSource.src = videoPath;
    preloadSource.type = "video/mp4";
    preloadVideo.appendChild(preloadSource);

    preloadVideo.oncanplaythrough = () => {
      source.src = videoPath;
      video.load();
      video.play();
    };
  }
}

// Handles radio button changes
function setBinary(id, value) {
  document.getElementById(id).value = value;
  toggleCapacityVisibility();
  updateMedia();
}

// Event listeners to update UI on page load
window.addEventListener("DOMContentLoaded", function () {
  updateMortalityLabel(document.getElementById("mortality_label"));
  toggleCapacityVisibility();
  updateMedia();

  document.getElementById("mortality_func").addEventListener("input", () => {
    toggleCapacityVisibility();
    updateMedia();
  });
});

// 🔥 Block accidental submit events
document.addEventListener(
  "submit",
  function (e) {
    e.preventDefault();
    e.stopPropagation();
  },
  true
);

// ✅ Prevent form-triggered reloads from Blocs’ injected structure
document.querySelectorAll("input[type='radio']").forEach((input) => {
  input.addEventListener("click", function (e) {
    if (e.target.form) {
      e.preventDefault();
    }
  });
});
