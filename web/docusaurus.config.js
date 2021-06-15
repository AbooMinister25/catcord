/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'Catcord',
  tagline: 'A minimal chat application that is interacted with using an API',
  url: 'https://catcord.catdevs.tk',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'cat-dev-group', // Usually your GitHub org/user name.
  projectName: 'catcord', // Usually your repo name.
  themeConfig: {
    darkMode: true,
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: false,
      respectPrefersColorScheme: true,

      switchConfig: {
        darkIcon: '  ',
        darkIconStyle: {
          marginTop: '1px',
        },
        lightIcon: '  ',
        lightIconStyle: {
          marginTop: '1px',
        },
      },
    },
    sidebarCollapsible: true,
    navbar: {
      title: 'Catcord',
      logo: {
        alt: 'Catcord',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/cat-dev-group/catcord',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Tutorial',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Discord',
              href: 'https://discord.gg/yt8s6C33fw',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/cat-dev-group/catcord',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Catcord, Inc.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/cat-dev-group/catcord/edit/main/web/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/cat-dev-group/catcord/edit/master/web/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
