module.exports = {
  mainSidebar: [
    {
      type: "category",
      label: "Intro",
      collapsed: false,
      items: ["intro", "frontend", "backend"],
    },
    {
      type: "category",
      label: "See Also",
      collapsed: false,
      items: ["see-also/contributing", "see-also/terms", "see-also/privacy"],
    },
  ],
  apiReferenceSidebar: [
    {
      type: "category",
      label: "Intro",
      collapsed: false,
      items: ["api/intro", "api/change-log"],
    },
    {
      type: "category",
      label: "Structures",
      collapsed: false,
      items: ["api/structures/users", "api/structures/servers", "api/structures/messages"],
    },
  ],
};
