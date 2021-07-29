<script context="module">
  // For some reason ESLint is reading this as TypeScript 😕
  /* eslint-disable-next-line */
  export function load({ status, error }) {
    return {
      props: {
        status: `${status}`,
        error: `${error.message}`,
      },
    };
  }
</script>

<script>
  export let status;
  export let error;
</script>

<div class="error-page">
  <h1>oops&#126;</h1>
  <h2>it seems we've run into an error</h2>
  <h2><strong>Status Code:</strong> {status}</h2>
  <h2><strong>Error:</strong> {error}</h2>
</div>

<style lang="scss">
  .error-page {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  
  h1 {
    font-size: 4rem;
  }
</style>
