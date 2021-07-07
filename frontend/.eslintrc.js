module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
    es2021: true
  },
  parserOptions: {
    sourceType: "module",
    parser: "babel-eslint",
    allowImportExportEverywhere: false,
    ecmaVersion: 2020,
    ecmaFeatures: {
      jsx: true,
    },
  },
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/eslint-recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  plugins: [
    "react",
  ],
  settings: {
    react: {
      version: "detect"
    }
  },
  rules: {
    "@typescript-eslint/explicit-module-boundary-types": "off",
    indent: ["error", 2],
    quotes: ["error", "double"],
    semi: ["error", "always"]
  },
};