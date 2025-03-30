const handleSubmit = async () => {
    const res = await fetch("http://localhost:8000/lesson/1/prompt-injection", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input })
    });
    const data = await res.json();
    setOutput(data.response);
}; 