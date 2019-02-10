package snakeinmyboot.soundboard

import com.google.gson.annotations.SerializedName
import io.reactivex.Observable
import retrofit2.http.Body
import retrofit2.http.POST

class WebInterface {

    interface SoundAPI {

        @POST("/soundboard")
        fun postAudio(@Body data: Data) : Observable<List<Data>>
    }

    data class Response(@SerializedName("name") val name: String)

    data class Data(@SerializedName("name") val name:String, @SerializedName("raw") val raw:String)
}
