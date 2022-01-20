<script lang="ts">
  import { _ } from "svelte-i18n";
  import axios from "axios";
  import Card, {
    Content,
    Media,
    MediaContent,
    PrimaryAction,
  } from "@smui/card";
  import { Link } from "svelte-routing";
  import Loading from "../api/Loading.svelte";
  import Pagination from "../api/Pagination.svelte";
  import SearchBar from "../api/SearchBar.svelte";
  import type { CoursesResponse, CourseList } from "./Api";

  const itemsPerPage = 12;

  let currentPage = 1;
  let numberOfItems = 0;
  let search = "";
  let courses: CourseList[] = [];
  let loading = true;

  function loadData() {
    loading = true;

    axios
      .get<CoursesResponse>(`${process.env.API_HOST}/api/courses/`, {
        params: {
          search,
          page: currentPage,
        },
      })
      .then((response) => {
        numberOfItems = response.data.count;
        courses = response.data.results;
      })
      .finally(() => {
        loading = false;
      });
  }

  loadData();
</script>

<section>
  <SearchBar bind:search on:change={() => loadData()} />

  {#if loading}
    <Loading />
  {:else}
    <div class="course-container">
      {#each courses as course}
        <Link class="anon" to="/{course.slug}">
          <Card>
            <PrimaryAction on:click={() => {}}>
              <Media class="card-media-square" aspectRatio="square">
                <MediaContent>
                  <img src={course.image} alt={course.name} />
                </MediaContent>
              </Media>
              <Content style="text-align: center">{course.name}</Content>
            </PrimaryAction>
          </Card>
        </Link>
      {/each}
    </div>
  {/if}

  <Pagination
    bind:currentPage
    {numberOfItems}
    {itemsPerPage}
    on:change={() => loadData()}
  />
</section>

<style>
  .course-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, 250px);
    gap: 10px;
    padding: 10px;
  }

  .course-container img {
    width: 80%;
    margin: auto;
    display: block;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
  }
</style>
