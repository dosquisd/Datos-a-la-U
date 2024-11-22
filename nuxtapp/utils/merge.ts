type CommonKey<T, U> = keyof T & keyof U;

type EnsureMatchingKey<T, U, K extends CommonKey<T, U>> = T[K] extends U[K]
    ? K
    : never;

interface MergeArgs<T, U, K extends CommonKey<T, U>> {
    initial: T[];
    other: U[];
    key: EnsureMatchingKey<T, U, K>;
}

export default function mergeArrays<
    T extends Record<string, unknown>,
    U extends Record<string, unknown>,
    K extends CommonKey<T, U>,
>({ initial, other, key }: MergeArgs<T, U, K>): Prettify<(T & Partial<U>)[]> {
    return initial.map((initialObject) => {
        const match = other.find(
            (otherObject) =>
                initialObject[key as keyof CommonKey<T, U>] ===
                otherObject[key as keyof CommonKey<T, U>],
        );
        return { ...initialObject, ...(match || {}) } as T & Partial<U>;
    });
}
