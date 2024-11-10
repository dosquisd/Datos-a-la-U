import rawData from "@/data/depts_mpios.json";
import { z } from "zod";

const CourtHouseData = z.object({
    courthouse: z.string(),
    lat: z.string(),
    lon: z.string(),
});

const MunicipalityData = z.record(
    z.string(),
    z.nullable(z.array(CourtHouseData)),
);

const DataShape = z.object({
    department: z.string(),
    municipalities: MunicipalityData,
});

const DataShapeArray = z.array(DataShape);

export default function () {
    const departments = computed<string[]>(() => {
        if (!rawData) return [];

        const parsedData = DataShapeArray.parse(rawData);

        const filteredData = parsedData.filter((item) => {
            return Object.values(item.municipalities).some(
                (value) => value !== null,
            );
        });

        return filteredData.map((item) => item.department);
    });

    return { departments };
}
