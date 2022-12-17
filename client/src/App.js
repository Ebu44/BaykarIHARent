import Header from "./components/Header";
import UAV from "./components/UAV";
import Model from "./components/Model";

function App() {
  return (
    <div className="App">
      <header className="container mx-auto">
        <Header />
        <UAV />
        <Model />
      </header>
    </div>
  );
}

export default App;
