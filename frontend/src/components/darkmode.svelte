<script lang="ts">
  import { onMount } from "svelte";
  onMount(() => {
    // @ts-ignore
    document.getElementById("theme-toggle")
      .addEventListener("click", function () {
        document.body.classList.toggle("light");
        document.body.classList.toggle("dark");
      });
  });
</script>

<button id="theme-toggle">Toggle Theme</button>