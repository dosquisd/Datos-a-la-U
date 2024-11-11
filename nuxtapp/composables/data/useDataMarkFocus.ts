export default function () {
    const modalActive = useState<boolean>(
        "mark-focused-modal-active",
        () => false,
    );
    const markData = useState<Mark | undefined>();
    
    return {
        modalActive,
        markData,
    };
}