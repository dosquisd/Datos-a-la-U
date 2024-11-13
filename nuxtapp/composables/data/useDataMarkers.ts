import { filteredData } from "@/schema/datashape";
import { z } from "zod";

const Response = z.object({
    courthouse: z.string(),
    lat: z.string(),
    lon: z.string(),
});

const ResponseArray = z.array(Response);

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

    function getDepartmentName(courthouseName: string): string | undefined {
        const item = filteredData.find((item) =>
            Object.values(item.municipalities).some((courtHouses) =>
                courtHouses?.some(
                    (courtHouse) => courtHouse.courthouse === courthouseName,
                ),
            ),
        );

        return item?.department;
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
