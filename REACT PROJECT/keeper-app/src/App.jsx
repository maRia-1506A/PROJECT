import React from "react";
import Header from "./Componenets/Header";
import Footer from "./Componenets/Footer";
import Note from "./Componenets/Note";
import notes from "./Notes";

function App() {
  return (
    < div >
      <Header />
      {/* array map function */}
      {notes.map((x) => (
        <Note
          key={x.key}
          title={x.title}
          content={x.content}
        />
      ))}
      <Footer />
    </div >
  );
}

export default App;