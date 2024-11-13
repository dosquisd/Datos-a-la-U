export default defineNuxtConfig({
    compatibilityDate: "2024-04-03",
    devtools: { enabled: true },
    modules: [
        "@nuxt/icon",
        "@nuxtjs/tailwindcss",
        [
            "shadcn-nuxt",
            {
                prefix: "",
                componentDir: "./components/ui",
            },
        ],
        "@nuxt/eslint",
        "@nuxtjs/leaflet",
        "@formkit/auto-animate",
        ["@nuxtjs/color-mode", { classSuffix: "" }],
        "@vueuse/motion/nuxt",
    ],
    runtimeConfig: {
        public: {
            apiBase: "http://localhost:8000",
        },
    },
    imports: {
        dirs: ["composables/**"],
    },
});
