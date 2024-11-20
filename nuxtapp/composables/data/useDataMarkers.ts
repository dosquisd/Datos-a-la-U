import { z } from "zod";

const Response = z.object({
    courthouse: z.string(),
    lat: z.string(),
    lon: z.string(),
});

const ResponseArray = z.array(Response);

const Department = z.object({
    department: z.string(),
});

export default function () {
    const marks = useState<Mark[] | undefined>();

    function makeMarks(department?: string) {
        $fetch("/data/courthouses", {
            baseURL: useRuntimeConfig().public.apiBase,
            query: {
                department,
            },
        })
            .then<z.infer<typeof ResponseArray>>((response) =>
                ResponseArray.parse(response),
            )
            .then<Mark[]>((response) =>
                response.map((item) => ({
                    lat: parseFloat(item.lat),
                    lon: parseFloat(item.lon),
                    name: item.courthouse,
                })),
            )
            .then((response) => (marks.value = response));
    }

    function getDepartmentName(courthouseName: string) {
        return $fetch("/data/department/courthouse", {
            baseURL: useRuntimeConfig().public.apiBase,
            query: {
                courthouse_name: courthouseName,
            },
        })
            .then<z.infer<typeof Department>>((response) =>
                Department.parse(response),
            )
            .then((response) => Promise.resolve(response.department));
    }

    onMounted(() => {
        const { department } = useOptions();

        watch(department, () => makeMarks(department.value));
    });

    return {
        marks,
        makeMarks,
        getDepartmentName,
    };
}
