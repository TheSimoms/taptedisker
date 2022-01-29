<script lang="ts">
  import Fa from "svelte-fa";
  import { faExpandArrowsAlt } from "@fortawesome/free-solid-svg-icons";
  import L from "leaflet";
  import type { CourseDetails } from "./Api";

  export let course: CourseDetails;

  const initialView = new L.LatLng(course.latitude, course.longitude);
  const initialZoom = 16;

  let map: L.Map;

  function addMap(container: HTMLElement) {
    map = new L.Map(container).setView(initialView, initialZoom);

    L.tileLayer("http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", {
      attribution: `Map data &copy; ${new Date().getFullYear()} Google`,
      minZoom: 15,
      maxZoom: 20,
      subdomains: ["mt0", "mt1", "mt2", "mt3"],
    }).addTo(map);

    map.on("click", onMapClick);
  }

  function onMapClick(event: L.LeafletMouseEvent) {
    console.log(event.latlng);
  }

  function resetMap() {
    map.setView(initialView, initialZoom);
  }
</script>

<svelte:head>
  <link rel="stylesheet" href="/node_modules/leaflet/dist/leaflet.css" />
</svelte:head>

<div class="map" use:addMap>
  <div class="leaflet-control-container">
    <div class="leaflet-top leaflet-right">
      <button class="refresh leaflet-bar leaflet-control" on:click={resetMap}>
        <Fa icon={faExpandArrowsAlt} />
      </button>
    </div>
  </div>
</div>

<style>
  .map {
    height: 600px;
  }

  @media (min-width: 1000px) {
    .map {
      max-width: 80%;
    }
  }

  .refresh {
    cursor: pointer;
    width: 2rem;
    height: 2rem;
  }
</style>
