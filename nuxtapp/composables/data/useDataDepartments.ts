import rawData from "@/data/depts_mpios.json";
import { filteredData } from "@/schema/datashape";

export default function () {
    const departments = computed<string[]>(() => {
        if (!rawData) return [];

        return filteredData.map((item) => item.department);
    });

    return { departments };
}
