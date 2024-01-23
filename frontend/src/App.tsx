import { useEffect, useState } from "react";
import complete from "./complete";

function App() {
    const [text, setText] = useState("");

    useEffect(() => {
        const completeText = async () => {
            const token = await complete(text);
            setText(`${text}${token}`);
        };

        const tabHandler = (e: KeyboardEvent) => {
            if (e.key === "Tab") {
                e.preventDefault();
                completeText();
            }
        };

        window.addEventListener("keydown", tabHandler);

        return () => {
            window.removeEventListener("keydown", tabHandler);
        };
    });

    return (
        <>
            <textarea
                value={text}
                onChange={(e) => setText(e.currentTarget.value)}
                name="text"
                cols={80}
                rows={60}
            ></textarea>
        </>
    );
}

export default App;
