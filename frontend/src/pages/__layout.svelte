<script lang="ts">
  import Navbar from "../components/navbar.svelte";
  import "../scss/globals.scss";
</script>

<header>
  <nav>
    <Navbar />
  </nav>
</header>
<main>
  <slot />
</main>