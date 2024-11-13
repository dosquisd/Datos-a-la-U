import { z } from "zod";

const Response = z.array(z.string());

export default function () {
    const { data, error } = useFetch<unknown>("/data/department", {
        baseURL: useRuntimeConfig().public.apiBase,
        method: "GET",
    });

    const departments = computed<z.infer<typeof Response> | undefined>(() => {
        if (!data.value) return;

        return Response.parse(data.value);
    });

    return {
        departments,
        error,
    };
}
