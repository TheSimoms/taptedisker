import svelte from "rollup-plugin-svelte";
import commonjs from "@rollup/plugin-commonjs";
import json from "@rollup/plugin-json";
import resolve from "@rollup/plugin-node-resolve";
import livereload from "rollup-plugin-livereload";
import { terser } from "rollup-plugin-terser";
import sveltePreprocess from "svelte-preprocess";
import typescript from "@rollup/plugin-typescript";
import css from "rollup-plugin-css-only";
import injectProcessEnv from 'rollup-plugin-inject-process-env';
import copy from 'rollup-plugin-copy'

const production = !process.env.ROLLUP_WATCH;

export default [
  {
    input: "src/main.ts",
    output: {
      sourcemap: true,
      format: "iife",
      name: "app",
      file: "public/bundle.js",
    },
    plugins: [
      svelte({
        preprocess: sveltePreprocess({ sourceMap: !production }),
        compilerOptions: {
          dev: !production,
        },
      }),
      css({ output: 'bundle.css' }),
      resolve({
        browser: true,
        dedupe: ['svelte']
      }),
      json(),
      commonjs(),
      typescript({
        sourceMap: !production,
        inlineSources: !production,
      }),
      injectProcessEnv({
        API_HOST: process.env.API_HOST,
      }),
      copy({
        targets: [
          {
            src: "node_modules/svelte-material-ui",
            dest: "public/node_modules",
          },
        ],
      }),

      !production && livereload('public'),

      production && terser(),
    ],
    watch: {
      clearScreen: false,
    },
  },
];
