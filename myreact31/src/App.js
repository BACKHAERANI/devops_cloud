import PageLotto from "./PageLotto ";
import ProfileCard from "./components/ProfileCard";
import { useState } from "react";
import profileImage1 from "./components/member1.jpg";
import profileImage2 from "./components/member2.jpg";
import profileImage3 from "./components/member3.jpg";
import profileImage4 from "./components/member4.jpg";
import TopNav from "./TopNav";

function App() {
  const [profilePage, setProfilePage] = useState();
  return (
    <div>
      <TopNav changePage={setProfilePage} />
      {profilePage === "Lotto" && <PageLotto />}
      <hr />
      {profilePage === "Profile1" && (
        <ProfileCard
          changePage={setProfilePage}
          name={"빨간머리 앤"}
          role={"배우"}
          profileImage={profileImage1}
          facebook_url={"1111.facebook"}
          email={"1111@naver.com"}
        />
      )}
      {profilePage === "Profile2" && (
        <ProfileCard
          changePage={setProfilePage}
          name={"박봄"}
          role={"가수"}
          profileImage={profileImage2}
          facebook_url={"2222.facebook"}
          email={"2222@naver.com"}
        />
      )}
      {profilePage === "Profile3" && (
        <ProfileCard
          changePage={setProfilePage}
          name={"누군가"}
          role={"래퍼"}
          profileImage={profileImage3}
          facebook_url={"3333.facebook"}
          email={"33334@naver.com"}
        />
      )}
      {profilePage === "Profile4" && (
        <ProfileCard
          changePage={setProfilePage}
          name={"fucci"}
          role={"photograper"}
          profileImage={profileImage4}
          facebook_url={"4444.facebook"}
          email={"4444@naver.com"}
        />
      )}
    </div>
  );
}

export default App;
