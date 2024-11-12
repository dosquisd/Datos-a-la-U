import { filteredData } from "@/schema/datashape";

export default function () {
    const marks = useState<Mark[] | undefined>();

    function makeMarks(department?: string) {
        if (!department) {
            marks.value = filteredData.flatMap((item) =>
                Object.values(item.municipalities)
                    .filter((courtHouseData) => courtHouseData !== null)
                    .flatMap((courtHouseData) =>
                        courtHouseData!.map((courtHouse) => ({
                            lat: parseFloat(courtHouse.lat),
                            lon: parseFloat(courtHouse.lon),
                            name: courtHouse.courthouse,
                        })),
                    ),
            );

            return;
        }

        const boundedData = filteredData.find(
            (item) => item.department === department,
        );

        if (!boundedData) return;

        marks.value = Object.values(boundedData.municipalities)
            .filter((courtHouseData) => courtHouseData !== null)
            .flatMap((courtHouseData) =>
                courtHouseData!.map((courtHouse) => ({
                    lat: parseFloat(courtHouse.lat),
                    lon: parseFloat(courtHouse.lon),
                    name: courtHouse.courthouse,
                })),
            );
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
