import { useState, useEffect } from "react";
import Axios from "axios";

function PageProfile() {
  const [profileList, setProfileList] = useState([]);
  const [checkError, setCheckError] = useState(null);

  const handleRefresh = () => {
    setCheckError(null);
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        const profileList = response.data.map((profile) => ({
          ...profile,
          unique: profile.unique_id,
          profileimageurl: profile.profile_image_url,
          instagramurl: profile.instagram_url,
        }));
        setProfileList(profileList);
      })
      .catch((error) => {
        setCheckError(error);
      });
  };

  useEffect(() => {
    handleRefresh();
  }, []);

  return (
    <div>
      <h2>PageProfile</h2>

      <button onClick={() => setProfileList([])}>clear</button>

      <button onClick={handleRefresh}>새로고침</button>

      {profileList.length == 0 && !checkError && (
        <h3>등록된 프로필이 없습니다.</h3>
      )}

      {checkError && <h3>오류가 발생했습니다. 잠시후 다시 시도해주세요.</h3>}

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
