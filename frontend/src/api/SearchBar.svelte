<script lang="ts">
  import { _ } from "svelte-i18n";

  export let search: string;
</script>

<input class="search-bar" placeholder="{$_('courses.search')}" bind:value={search} on:change />

<style>
  .search-bar {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
    margin-top: 1.25em;
    margin-bottom: 2em;
  }
</style>
