package snakeinmyboot.soundboard

import android.content.Context
import android.os.Environment
import android.util.Log
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.Button
import java.io.File

class BoardAdapter(val context: Context, val sounds: List<String>, val boardMediaInterface: BoardMediaInterface): BaseAdapter() {

    private val TAG = "BoardDebug"

    override fun getCount(): Int {
        return sounds.size
    }

    override fun getItem(position: Int): Any {
        return sounds[position]
    }

    override fun getItemId(position: Int): Long {
        return Long.MAX_VALUE
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val button = Button(context)
        var text = sounds[position].replace(Environment.getExternalStorageDirectory().toString() + "/soundboard/", "").substringBefore('.')
        button.text = text
        button.setOnClickListener({
            val file = File(sounds[position])
            Log.d(TAG, file.toString())
            boardMediaInterface.playMedia(file)
        })
        return button
    }

    interface BoardMediaInterface{

        fun playMedia(file : File)
    }

}