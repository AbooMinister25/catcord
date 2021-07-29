/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: "Catcord",
  tagline: "An open-source chat app",
  url: "https://catcord.codes",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "cat-dev-group",
  projectName: "catcord",
  themeConfig: {
    darkMode: true,
    colorMode: {
      defaultMode: "dark",
      disableSwitch: false,
      respectPrefersColorScheme: true,

      switchConfig: {
        darkIcon: "  ",
        darkIconStyle: {
          marginTop: "1px",
        },
        lightIcon: "  ",
        lightIconStyle: {
          marginTop: "1px",
        },
      },
    },
    image: "/img/docusaurus.png",
    hideOnScroll: true,
    navbar: {
      title: "Catcord",
      logo: {
        alt: "Catcord Logo",
        src: "img/logo.svg",
      },
      items: [
        {
          type: "doc",
          docId: "intro",
          position: "left",
          label: "Docs",
        },
        {
          type: "doc",
          docId: "api/intro",
          position: "left",
          label: "API Reference",
        },
        {
          href: "https://github.com/cat-dev-group/catcord",
          className: "navbar-item-github",
          position: "right",
        },
      ],
    },
    footer: {
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Intro",
              to: "/",
            },
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "Discord",
              href: "https://discord.gg/tRRSARGMCy",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/cat-dev-group/catcord",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Catcord Contributors`,
    },
    prism: {
      defaultLanguage: "js",
      plugins: ["line-numbers", "show-language"],
    },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          routeBasePath: "/",
          editUrl: "https://github.com/cat-dev-group/catcord/blob/main/docs/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
};
