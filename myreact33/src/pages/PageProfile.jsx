import { useState } from "react";

function PageProfile() {
  const [profileList] = useState([
    // {
    //   unique: "bts-jin",
    //   name: "진",
    //   role: "서브보컬",
    //   mbti: "INFP",
    //   instagramurl: "https://instagram.com/jin",
    //   profileimageurl:
    //     "https://classdevopscloud.blob.core.windows.net/data/bts-jin.jpg",
    // },
  ]);

  return (
    <div>
      <h2>PageProfile</h2>

      {profileList.length == 0 && <h3>등록된 프로필이 없습니다.</h3>}

      {profileList.map((member) => {
        return (
          <>
            <h3>
              [{member.unique}]{member.name}
            </h3>
            <ul>
              <img src={member.profileimageurl} />
              <li>{member.role}</li>
              <li>{member.instagramurl}</li>
              <li>{member.mbti}</li>
            </ul>
          </>
        );
      })}
    </div>
  );
}

export default PageProfile;
