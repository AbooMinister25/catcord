<script lang="ts">
  import DarkMode from "./darkmode.svelte";
</script>

<div id="wrapper">
  <div id="a">
    <div id="b">
      <div id="c">
        <div id="d1">
          <a href="/">Catcord</a>
        </div>
        <div id="d2">
          <a href="https://docs.catcord.codes">Docs</a>
        </div>
      </div>
      <DarkMode />
    </div>
  </div>
</div>

<style lang="scss">
  @import "../scss/themes";

  a {
    cursor: pointer;
    color: var(--text-color);
  }

  #wrapper {
    border-bottom: 1px solid var(--nav-border-color);
    position: sticky;
    top: 0;
  }

  #a {
    margin: auto;
    position: relative;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    height: 4rem;
    border-bottom-style: none;

    @media (min-width: 1024px) {
      padding-left: 4rem;
      padding-right: 4rem;
    }

    @media (min-width: 1280px) {
      padding-left: 5rem;
      padding-right: 5rem;
    }
  }

  #b {
    display: flex;
    flex-wrap: wrap;
    flex: 1 1 0%;
    align-items: center;
    justify-content: center;
    justify-content: space-between;
  }

  #c {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    display: flex;
    flex-wrap: wrap;
  }

  #d1 {
    display: flex;
    flex-wrap: wrap;
    flex-shrink: 0;
    font-weight: 500;
    padding: 1rem;
  }

  #d2 {
    padding: 1rem;
    display: flex;
    flex-wrap: wrap;
  }
</style>
