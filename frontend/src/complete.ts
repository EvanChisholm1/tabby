const complete = async (text: string): Promise<string> => {
    const res = await fetch("http://localhost:8080/complete", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text,
        }),
    });

    const json = await res.json();

    console.log(json.token);
    return json.token;
};

export default complete;
