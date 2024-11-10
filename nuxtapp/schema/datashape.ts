import rawData from "@/data/depts_mpios.json";
import { z } from "zod";

export const CourtHouseData = z.object({
    courthouse: z.string(),
    lat: z.string(),
    lon: z.string(),
});

export const MunicipalityData = z.record(
    z.string(),
    z.nullable(z.array(CourtHouseData)),
);

export const DataShape = z.object({
    department: z.string(),
    municipalities: MunicipalityData,
});

export const DataShapeArray = z.array(DataShape);

export const parsedData = DataShapeArray.parse(rawData);

export const filteredData = parsedData.filter((item) => {
    return Object.values(item.municipalities).some((value) => value !== null);
});
