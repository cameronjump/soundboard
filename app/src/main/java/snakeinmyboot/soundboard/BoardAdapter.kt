package snakeinmyboot.soundboard

import android.content.Context
import android.os.Environment
import android.support.v4.content.ContextCompat.getColor
import android.util.Log
import android.view.View
import android.view.ViewGroup
import java.io.File
import android.R.attr.bottom
import android.R.attr.right
import android.R.attr.top
import android.R.attr.left
import android.support.v4.content.ContextCompat.getDrawable
import android.view.WindowManager
import android.widget.*


class BoardAdapter(val context: Context, val sounds: List<String>, val boardMediaInterface: BoardMediaInterface, val baseurl: String): BaseAdapter() {

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
        var text = sounds[position].replace(baseurl, "").substringBefore('.')
        button.text = text
        button.setTextColor(getColor(context,R.color.white))
        button.background = getDrawable(context, R.drawable.grid_button)
        button.setOnClickListener{
            val file = File(sounds[position])
            Log.d(TAG, file.toString())
            boardMediaInterface.playMedia(file)
        }
        button.setOnLongClickListener {
            val file = File(sounds[position])
            file.delete()
            boardMediaInterface.addAdapter()
            true
        }
        return button
    }

    interface BoardMediaInterface{

        fun playMedia(file : File)

        fun addAdapter()
    }

}