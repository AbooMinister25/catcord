import preprocess from "svelte-preprocess";
import node from "@sveltejs/adapter-node";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: preprocess(),
  kit: {
    adapter: node({out: "dist"}),
    target: "#svelte",
    files: {
      assets: "public",
      hooks: "src/hooks",
      lib: "src/lib",
      routes: "src/pages",
      serviceWorker: "src/service-worker",
      template: "src/index.html",
    },
  },
};

export default config;
