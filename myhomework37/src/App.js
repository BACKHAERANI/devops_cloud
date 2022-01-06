import PageReview from 'pages/PageReview';
import TopNav from 'compoents/TopNav';
import { Routes, Route } from 'react-router-dom';
import PageNotFound from 'pages/PageNotFound';

function App() {
  return (
    <div>
      <TopNav />
      <Routes>
        <Route path="/" element={<div>H...om...e</div>} />
        <Route path="/reviews" element={<PageReview />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </div>
  );
}

export default App;
