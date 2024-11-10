import rawData from "@/data/depts_mpios_tmp.json";
import { z } from "zod";

const DataShape = z.object({
    department: z.string(),
});

const DataShapeArray = z.array(DataShape);

export default function () {
    const departments = computed<string[]>(() => {
        if (!rawData) return [];

        const parsedData = DataShapeArray.parse(rawData);

        return parsedData.map((item) => item.department);
    });

    return { departments };
}
