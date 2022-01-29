<script lang="ts">
  import { _ } from "svelte-i18n";
  import axios from "axios";
  import type { CourseDetails } from "./Api";
  import Loading from "../api/Loading.svelte";
  import Map from "./Map.svelte";

  export let slug: string;

  const coursePromise: Promise<CourseDetails> = axios
      .get<CourseDetails>(`${process.env.API_HOST}/api/courses/${slug}`)
      .then((response) => response.data);
</script>

{#await coursePromise}
	<Loading />
{:then course}
  <h1>{course.name}</h1>

  <Map {course} />
{:catch}
  <p>{$_('fetch.error')}</p>
{/await}
