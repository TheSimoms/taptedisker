<script lang="ts">
  import { init, getLocaleFromNavigator, addMessages } from "svelte-i18n";
  import { Router, Route } from "svelte-routing";

  import en from "../public/lang/en.json";
  import no from "../public/lang/no.json";

  addMessages("en-UK", en);
  addMessages("nb", no);
  addMessages("nn", no);
  addMessages("no", no);
  addMessages("nb-NO", no);
  addMessages("nn-NO", no);

  init({
    fallbackLocale: "en-UK",
    initialLocale: getLocaleFromNavigator(),
  });

  import Menu from "./Menu.svelte";
  import Courses from "./courses/Courses.svelte";
  import CourseInfo from "./courses/CourseInfo.svelte";

  export let url = '';
</script>

<Router {url}>
  <Menu />

  <main>
    <Route path="/:slug" component="{CourseInfo}" />
    <Route path="/"><Courses /></Route>
  </main>
</Router>
