export {};

declare global {
    interface Mark {
        lat: number;
        lon: number;
        name: string;
    }

    type Prettify<T> = {
        [K in keyof T]: T[K];
    } & {};
}
